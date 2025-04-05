def main():
    filename = input("Enter the filename to read from: ")

    try:
        with open(filename, "r") as file:
            content = file.read()

        modified_content = content.upper()

        with open("output.txt", "w") as outfile:
            outfile.write(modified_content)

        print("✅ Success! Modified content written to 'output.txt'.")

    except FileNotFoundError:
        print("❌ Error: File not found.")
    except Exception as e:
        print(f"❌ An error occurred: {e}")

if __name__ == "__main__":
    main()