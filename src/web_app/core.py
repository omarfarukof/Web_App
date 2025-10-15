from dataclasses import dataclass, field, asdict
from pathlib import Path
from typing import Optional
import urllib.request
import urllib.parse
from importlib import resources
from jinja2 import Environment, FileSystemLoader
import shutil
import os


@dataclass(slots=True)
class WebApp:
    """Represents a .desktop Web-App entry."""
    name: str
    url: str
    browser: str = "chromium"
    app_paths: dict[str, str | Path] = field(default_factory=lambda: {
        "desktop": "" ,
        "sh": "" ,
        "app": "",
        "icon": "",
        "profile": "",
        "web": ""})

    version: str = "1.0"
    comment: str = "Web App"
    terminal: bool = False
    startup_wm_class: Optional[str] = None
    isolated: bool = True
    private: bool = False
    navbar: bool = False
    categories: str = "WebApps;"
    mime_types: str = ""
    startup_notify: bool = True

    def get_dict(self):
        return asdict(self)

    def _get_app_id(self):
        return f"{self.name}_web_app"
    def _get_paths(self):
        APP_ID = self._get_app_id()
        HOME_DATA = Path(os.environ.get("XDG_DATA_HOME", Path.home()/".local/share")) 
        HOME_BIN = Path.home()/".local/bin" 
        APP_DIR = HOME_DATA / APP_ID
        APP_DATA = APP_DIR / "data"
        WEB_BIN = HOME_BIN / "Web_Apps"
        APP_SH = WEB_BIN / f"{APP_ID}.sh"
        APP_ICON = APP_DIR / f"{APP_ID}.png"
        APP_DESKTOP = HOME_DATA / "applications" / f"{APP_ID}.desktop"

        return {
            "desktop": APP_DESKTOP ,
            "sh": APP_SH ,
            "app": APP_DIR,
            "icon": APP_ICON,
            "profile": APP_DATA,
            "web": WEB_BIN
        }

    def app_init(self):
        self.app_paths = self._get_paths()

    def to_sh(self) -> str:
        tpl_dir = resources.files("web_app") / "templates"
        env = Environment(loader=FileSystemLoader(tpl_dir), autoescape=False)
        tmp = env.get_template("name_web_app.sh.j2")
        return tmp.render(self.get_dict())

    def to_desktop_entry(self) -> str:
        tpl_dir = resources.files("web_app") / "templates"
        env = Environment(loader=FileSystemLoader(tpl_dir), autoescape=False)
        tmp = env.get_template("name_web_app.desktop.j2")
        return tmp.render(self.get_dict())

    # TODO: Add option to insert Custom icon
    def download_icon(self):
        """Best-effort favicon grabber (falls back to default)."""
        try:
            domain = urllib.parse.urlparse(self.url).netloc
            for fmt in ["png", "ico"]:
                try:
                    icon_url = f"https://www.google.com/s2/favicons?domain={domain}&sz=128"
                    urllib.request.urlretrieve(icon_url, self.app_paths["icon"])
                    return
                except Exception:
                    continue
        except Exception:
            pass

    def create_app(self):
        self.app_paths["app"].mkdir(parents=True, exist_ok=True)
        self.download_icon()

        sh_file = Path(self.app_paths["sh"]).resolve()
        sh_file.parent.mkdir(parents=True, exist_ok=True)
        sh_file.write_text(self.to_sh())
        sh_file.chmod(0o755)

        desktop_entry = Path(self.app_paths["desktop"]).resolve()
        desktop_entry.parent.mkdir(parents=True, exist_ok=True)
        desktop_entry.write_text(self.to_desktop_entry())
        desktop_entry.chmod(0o755)

    def delete(self, full=False):
        if full:
            shutil.rmtree(self.app_paths["app"])
        else:
            sh_file = Path(self.app_paths["sh"])
            sh_file.unlink(missing_ok=True)

            desktop_file = Path(self.app_paths["desktop"])
            desktop_file.unlink(missing_ok=True)

    # TODO: List - All WebApps


    # TODO: Edit - A Selected WebApp