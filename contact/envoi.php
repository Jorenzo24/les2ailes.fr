<?php
/**
 * Traitement du formulaire de contact.
 *
 * Envoi via SMTP authentifié. La configuration est lue dans un .env placé
 * HORS du dossier web (/home/les2ailes/.env), jamais dans le dépôt.
 *
 * Répond en JSON si la requête vient du fetch() de main.js, sinon renvoie
 * l'utilisateur sur /contact/ avec un paramètre, pour que le formulaire
 * fonctionne aussi sans JavaScript.
 */

declare(strict_types=1);

const DEST_PAGE = '/contact/';

// ---------------------------------------------------------------- Réponse --
function estAjax(): bool
{
    $accept = $_SERVER['HTTP_ACCEPT'] ?? '';
    $xhr = $_SERVER['HTTP_X_REQUESTED_WITH'] ?? '';
    return strpos($accept, 'application/json') !== false || $xhr === 'fetch';
}

function repondre(bool $ok, string $message, int $code = 200): void
{
    if (estAjax()) {
        http_response_code($code);
        header('Content-Type: application/json; charset=utf-8');
        echo json_encode(['ok' => $ok, 'message' => $message], JSON_UNESCAPED_UNICODE);
    } else {
        header('Location: ' . DEST_PAGE . '?envoi=' . ($ok ? 'ok' : 'erreur'), true, 303);
    }
    exit;
}

// ------------------------------------------------------------------- .env --
function chargerEnv(): array
{
    $candidats = [
        dirname(__DIR__, 2) . '/.env',   // /home/les2ailes/.env  (recommandé)
        dirname(__DIR__) . '/.env',      // racine du site, à défaut
    ];
    foreach ($candidats as $chemin) {
        if (!is_readable($chemin)) {
            continue;
        }
        $env = [];
        foreach (file($chemin, FILE_IGNORE_NEW_LINES | FILE_SKIP_EMPTY_LINES) as $ligne) {
            $ligne = trim($ligne);
            if ($ligne === '' || $ligne[0] === '#' || strpos($ligne, '=') === false) {
                continue;
            }
            [$cle, $valeur] = explode('=', $ligne, 2);
            $env[trim($cle)] = trim($valeur);
        }
        return $env;
    }
    return [];
}

// ------------------------------------------------------------ Vérifications --
if (($_SERVER['REQUEST_METHOD'] ?? '') !== 'POST') {
    repondre(false, 'Méthode non autorisée.', 405);
}

// Pot de miel : un robot remplit tous les champs, un humain ne voit pas celui-ci.
if (trim((string) ($_POST['website'] ?? '')) !== '') {
    repondre(true, 'Message envoyé.');   // on ne dit rien au robot
}

$nom     = trim((string) ($_POST['nom'] ?? ''));
$email   = trim((string) ($_POST['email'] ?? ''));
$message = trim((string) ($_POST['message'] ?? ''));

if ($nom === '' || $email === '' || $message === '') {
    repondre(false, 'Merci de remplir tous les champs.', 422);
}
if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
    repondre(false, 'L’adresse e-mail ne semble pas valide.', 422);
}
if (mb_strlen($nom) > 120 || mb_strlen($email) > 180 || mb_strlen($message) > 5000) {
    repondre(false, 'Message trop long.', 422);
}
// Injection d'en-têtes
if (preg_match('/[\r\n]/', $nom . $email)) {
    repondre(false, 'Requête invalide.', 422);
}

// Limitation basique : un envoi toutes les 30 secondes par adresse IP.
$verrou = sys_get_temp_dir() . '/les2l-' . md5((string) ($_SERVER['REMOTE_ADDR'] ?? ''));
if (is_file($verrou) && (time() - filemtime($verrou)) < 30) {
    repondre(false, 'Merci de patienter quelques secondes avant un nouvel envoi.', 429);
}
touch($verrou);

// ------------------------------------------------------------------ Envoi --
$env = chargerEnv();
foreach (['SMTP_HOST', 'SMTP_PORT', 'SMTP_USER', 'SMTP_PASS', 'MAIL_FROM', 'MAIL_TO'] as $cle) {
    if (empty($env[$cle])) {
        error_log('[contact] .env introuvable ou incomplet : ' . $cle);
        repondre(false, 'Le formulaire est momentanément indisponible. Écrivez-nous directement à les2ailespy@gmail.com.', 500);
    }
}

require __DIR__ . '/../lib/PHPMailer/Exception.php';
require __DIR__ . '/../lib/PHPMailer/PHPMailer.php';
require __DIR__ . '/../lib/PHPMailer/SMTP.php';

$mail = new PHPMailer\PHPMailer\PHPMailer(true);

try {
    $mail->isSMTP();
    $mail->Host       = $env['SMTP_HOST'];
    $mail->Port       = (int) $env['SMTP_PORT'];
    $mail->SMTPAuth   = true;
    $mail->Username   = $env['SMTP_USER'];
    $mail->Password   = $env['SMTP_PASS'];
    $mail->SMTPSecure = ($env['SMTP_SECURE'] ?? 'tls') === 'ssl'
        ? PHPMailer\PHPMailer\PHPMailer::ENCRYPTION_SMTPS
        : PHPMailer\PHPMailer\PHPMailer::ENCRYPTION_STARTTLS;
    $mail->Timeout    = 15;
    $mail->CharSet    = 'UTF-8';

    $mail->setFrom($env['MAIL_FROM'], $env['MAIL_FROM_NAME'] ?? 'Site Les2L');
    $mail->addAddress($env['MAIL_TO'], $env['MAIL_TO_NAME'] ?? '');
    // Laurence répond directement au visiteur.
    $mail->addReplyTo($email, $nom);

    $mail->Subject = 'Message depuis le site : ' . $nom;
    $mail->Body    = "Nom : {$nom}\n"
                   . "E-mail : {$email}\n"
                   . "Date : " . date('d/m/Y à H:i') . "\n"
                   . "\n---\n\n{$message}\n";

    $mail->send();
    repondre(true, 'Merci, votre message est bien parti. Nous vous répondons rapidement.');
} catch (Throwable $e) {
    error_log('[contact] échec SMTP : ' . $e->getMessage());
    repondre(false, 'L’envoi a échoué. Écrivez-nous directement à les2ailespy@gmail.com.', 500);
}
