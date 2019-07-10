import identicon
s = "Y21614015"
img= identicon.render_identicon(abs(hash(s)) % (10 ** 20), 20)
img.save('2.png')