import os
import importlib.util
from colorama import init, Fore, Style

init(autoreset=True)

ADDONS_DIR = "addons"

def show_banner():
    banner = f"""
{Fore.CYAN}{Style.BRIGHT}
     ╔════════════════════════════════════════════╗
     ║      {Fore.MAGENTA}🛠  PYTHON-ADDON-FRAMEWORK             {Fore.CYAN}║
     ║      {Fore.YELLOW}github.com/{Fore.GREEN}AhmetFurkanUcak            {Fore.CYAN}║
     ╚════════════════════════════════════════════╝
{Style.RESET_ALL}
    """
    print(banner)


def load_addons():
    """Loads addons from the addons directory."""
    addons = []
    for filename in os.listdir(ADDONS_DIR):
        if filename.endswith(".py"):
            module_name = filename[:-3]
            module_path = os.path.join(ADDONS_DIR, filename)

            spec = importlib.util.spec_from_file_location(module_name, module_path)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)

            if hasattr(module, "run") and hasattr(module, "name"):
                addons.append(module)

    return addons

def main():
    show_banner()

    addons = load_addons()

    if not addons:
        print(Fore.RED + "No addons found!")
        return

    while True:
        print(Fore.BLUE + "\n[Loaded Addons]")
        for index, addon in enumerate(addons, start=1):
            print(Fore.GREEN + f"{index}. {addon.name}")

        print(Fore.YELLOW + "\n0. Run All Addons")
        print(Fore.YELLOW + "Q. Quit")

        try:
            choice = input(Fore.CYAN + "\nEnter the number of the addon to run (or 'Q' to quit): ").strip().lower()
            if choice == 'q':
                print(Fore.MAGENTA + "Exiting...")
                break

            choice = int(choice)

            if choice == 0:
                print(Fore.CYAN + "\nRunning all addons...\n")
                for addon in addons:
                    print(Fore.GREEN + f"Running {addon.name}...")
                    addon.run()
            elif 1 <= choice <= len(addons):
                selected_addon = addons[choice - 1]
                print(Fore.GREEN + f"\nRunning {selected_addon.name}...")
                selected_addon.run()
            else:
                print(Fore.RED + "Invalid choice! Please enter a valid number.")

        except ValueError:
            print(Fore.RED + "Please enter a valid number!")

if __name__ == "__main__":
    main()