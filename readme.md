<h2>Email Sender, 👋</h2>
<p>
    Bu "repo"da python orqali email pochtaga xabar yuborishingiz mumkin
</p>
<div class="row">
    ###### Dastlab "class"imizdan obyekt yaratib olamiz
    <hr>
    <code>email = Email(MY_EMAIL, APP_PASSWORD)</code>
</div>
<br>
<div class="row">
    ###### Kimningdir pochtasiga oddiygina habar yuborish
    <hr>
    <code>email.send_text('misol@uchun.uz', <mark>'sizning xabaringiz'</mark>)</code>
</div>
<br>
<div class="row">
    ###### Kimningdir pochtasiga file ko'rishidagi habar yuborish uchun
    <hr>
    <code>email.send_file('misol@uchun.uz', <mark>"faylning_joylashuvi"</mark>)</code>
</div>
<br>
<div class="row">
    ###### Habarni mavzu bilan yuborish
    <hr>
    <code>email.send_text('misol@uchun.com', 'text', <mark>subject="Habar Matni")</mark></code>
</div>
<br>
<div class="row">
    ###### Gipermatinli(HTML) habar yuborish
    <hr>
    <code>email.send_text('misol@uchun.com', <mark>'&lth1&gtSalom&lt/h1&gt&ltimg src="https://pictures.com/example.jpg"&gt'</mark>, subject="TEXT - ko'rinishidagi habar", <mark>type_='html'</mark></code>)
</div>
