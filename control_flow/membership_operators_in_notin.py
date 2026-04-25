# Security check for banned domain

domain='spam.com'
banned_domain=['spam.com','fake.com','bot.net']
print(f"Domain is safe: {domain not in banned_domain}")