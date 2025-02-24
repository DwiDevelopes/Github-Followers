from github import Github

# Ganti dengan token GitHub Anda
GITHUB_TOKEN = "your_github_token_here"

# Inisialisasi objek Github
g = Github(GITHUB_TOKEN)

# Mendapatkan informasi akun GitHub Anda
user = g.get_user()
print(f"Logged in as: {user.login}")

# Mendapatkan daftar followers
followers = user.get_followers()
print(f"Total followers: {followers.totalCount}")

# Contoh: Mengikuti pengguna lain
target_user = g.get_user("target_username")
user.add_to_following(target_user)
print(f"Started following: {target_user.login}")

# Contoh: Berhenti mengikuti pengguna
user.remove_from_following(target_user)
print(f"Stopped following: {target_user.login}")