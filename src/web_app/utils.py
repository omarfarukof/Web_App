# import shutil
# from pathlib import Path
# import os
# import sys

# # APP_ID_CHARSET = string.ascii_letters + string.digits
# # DEFAULT_ICON   = Path(__file__).with_name("icons") / "default.png"

# # def random_id(k=8): return ''.join(random.choices(APP_ID_CHARSET, k=k))

# # def sanitize(name:str)->str:
# #     return ''.join(c if c.isalnum() else '_' for c in name)

# def get_app_id(app_name: str):
#     return app_name+"_web_app"

# def get_dirs(app_name: str):
#     data = Path(os.environ.get("XDG_DATA_HOME", Path.home()/".local/share")) / get_app_id(app_name)
#     return {
#         "desktop": Path.home()/".local/share/applications"/get_app_id(app_name)+".desktop" ,
#         "sh": Path.home()/".local/bin"/get_app_id(app_name) ,
#         "app-data":   data,
#         "icon": data/ "icon",
#         "profile": data/ "profile"
#     }
    
# def detect_browser():
#     browser = {}
#     for b in ("chromium", "chromium-browser", "google-chrome", "microsoft-edge", "helium-browser" , "firefox"):
#         browser[b] = shutil.which(b)
#     return browser

# # def download_icon(url:str, dest:Path):
# #     """Best-effort favicon grabber (falls back to default)."""
# #     try:
# #         import urllib.request, urllib.parse
# #         domain = urllib.parse.urlparse(url).netloc
# #         for fmt in ["png", "ico"]:
# #             try:
# #                 icon_url = f"https://www.google.com/s2/favicons?domain={domain}&sz=128"
# #                 urllib.request.urlretrieve(icon_url, dest)
# #                 return
# #             except Exception:
# #                 continue
# #     except Exception:
# #         pass
# #     shutil.copy(DEFAULT_ICON, dest)