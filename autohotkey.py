from ahk import AHK

def main():
  ahk = AHK()
  script = ""
  try:
    with open("getter.ahk", 'r') as f:
      script = f.read()
      f.close()
  except FileNotFoundError:
      FileNotFoundError: "Could not read getter.ahk"

  ahk.run_script(script)

if __name__ == "__main__":
    main()