import argparse
from urllib.parse import urlparse
from pathlib import Path

# Internal
from web_app.core import WebApp


def main():
    """CLI entry point."""
    parser = argparse.ArgumentParser(description="Create a web application.")

    parser.add_argument("--name", required=True, help="The Name of the web application.")
    parser.add_argument("--url", required=True, help="The URL of the web application.")
    parser.add_argument("--browser", default="helium-browser", help="The browser to use.")
    parser.add_argument("--icon", default="", help="The path to the icon for the web application.")
    parser.add_argument("--private", action="store_true", default=True, help="Open in a private window.")
    parser.add_argument("--profile", default="", help="The browser profile to use.")

    args = parser.parse_args()

    # Create WebApp instance
    web_app = WebApp(
        name=args.name,
        url=args.url
    )
    web_app.app_init()

    web_app.browser = args.browser
    web_app.private = args.private
    if args.profile:
        web_app.app_paths["profile"]

    # TODO: ADD Custom ICON





    # # TEST: web_app
    # print(f"Web APP: {web_app.name}\n")
    # d = web_app.get_dict()
    # for k, v in d.items():
    #     if isinstance(v, dict):
    #         print("+",k,":")
    #         for _k, _v in v.items():
    #             print(f"\t{_k}: {_v}")
    #     else:
    #         print(f"{k}: {v}")


    # Create the application
    web_app.create_app()
    
    print(f"Web application '{args.name}' created successfully.")
    print(f"Add Web_Apps to your path. `export PATH=\"{web_app.app_paths["web"]}\"")


if __name__ == "__main__":
    main()
