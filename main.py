import os
import importlib.util

ADDONS_DIR = "addons"

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
    addons = load_addons()

    if not addons:
        print("No addons found!")
        return

    while True:
        print("\n[Loaded Addons]")
        for index, addon in enumerate(addons, start=1):
            print(f"{index}. {addon.name}")

        print("\n0. Run All Addons")
        print("Q. Quit")

        try:
            choice = input("\nEnter the number of the addon to run (or 'Q' to quit): ").strip().lower()
            if choice == 'q':
                print("Exiting...")
                break

            choice = int(choice)

            if choice == 0:
                print("\nRunning all addons...\n")
                for addon in addons:
                    print(f"Running {addon.name}...")
                    addon.run()
            elif 1 <= choice <= len(addons):
                selected_addon = addons[choice - 1]
                print(f"\nRunning {selected_addon.name}...")
                selected_addon.run()
            else:
                print("Invalid choice! Please enter a valid number.")

        except ValueError:
            print("Please enter a valid number!")

    # Auto Run All Addons
    # for addon in addons:
    #     print(f"{addon.name} Running...")
    #     addon.run()

if __name__ == "__main__":
    main()

