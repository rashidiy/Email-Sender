<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
</head>
<body style="background: #000;">
    <h2>Email Sender, 👋</h2>
    <p>
        Bu "repo"da python orqali email pochtaga xabar yuborishingiz mumkin
    </p>
    <div class="row">
        <hr>
        <label>Dastlab "class"imizdan obyekt yaratib olamiz</label>
        <code>email = Email(MY_EMAIL, APP_PASSWORD)</code>
    </div>
    <br>
    <div class="row">
        <hr>
        <label>Kimningdir pochtasiga oddiygina habar yuborish</label>
        <code>email.send_text('misol@uchun.uz', <mark style="color: yellow;">'sizning xabaringiz'</mark>)</code>
    </div>
    <br>
    <div class="row">
        <hr>
        <label>Kimningdir pochtasiga file ko'rishidagi habar yuborish uchun</label>
        <code>email.send_file('misol@uchun.uz', <mark>"faylning_joylashuvi"</mark>)</code>
    </div>
    <br>
    <div class="row">
        <hr>
        <label>Habarni mavzu bilan yuborish</label>
        <code>email.send_text('misol@uchun.com', 'text', <mark>subject="Habar Matni")</mark></code>
    </div>
    <br>
    <div class="row">
        <hr>
        <label>Gipermatinli(HTML) habar yuborish</label>
        <code>email.send_text('misol@uchun.com', <mark>'&lth1&gtSalom&lt/h1&gt&ltimg src="https://pictures.com/example.jpg"&gt'</mark>, subject="TEXT - ko'rinishidagi habar", <mark>type_='html'</mark></code>)
    </div>
</body>
</html>
