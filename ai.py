"""
Project Name - Suizen Task Bot (An Attempt to Make an A.I :D)

Author/DEV - Arsh_DEV

"""

#Main Code Starts :D
import time
import os
import webbrowser
import subprocess

 
head = '''                                                        
                                                        
////////   //    //  ////////   /////  //////  ////   //
//         //    //     //        //   //      // //  //
///////    //    //     //       //    //////  // //  //
     //    //    //     //      //     //      //  // //
///////    ////////  ////////  /////   //////  //   ////'''

def sec():
    os.system("CLS")
    time.sleep(2)
    print(head)
    print()
    con3 = input("Where Do you want to go ?\n\n[1] = Norton\n[2] = Avast Anti-Virus\n[3] = Quick Heal\n[4] = Back\n\n")
    if con3 == "1":
        time.sleep(2)
        webbrowser.open("https://in.norton.com/")
        time.sleep(2)
        main()
    elif con3 == "2":
        time.sleep(2)
        webbrowser.open("https://www.avast.com/")
        time.sleep(2)
        main()
    elif con3 == "3":
        time.sleep(2)
        webbrowser.open("https://www.quickheal.com/")
        time.sleep(2)
        main()
    elif con3 == "4":
        main()
    else:
        sec()

def ser():
    os.system("CLS")
    time.sleep(2)
    print(head)
    print()
    con2 = input("Where Do you want to go ?\n\n[1] = Netflix\n[2] = Prime Video\n[3] = YouTube\n[4] = Back\n\n")
    if con2 == "1":
        time.sleep(2)
        webbrowser.open("https://www.netflix.com/in/")
        time.sleep(2)
        main()
    elif con2 == "2":
        time.sleep(2)
        webbrowser.open("https://www.primevideo.com/")
        time.sleep(2)
        main()
    elif con2 == "3":
        time.sleep(2)
        webbrowser.open("https://youtube.com/")
        time.sleep(2)
        main()
    elif con2 == "4":
        main()
    else:
        ser()

def edu():
    os.system("CLS")
    time.sleep(2)
    print(head)
    print()
    con1 = input("Where Do you want to go ?\n\n[1] = DPS Patna\n[2] = Byjus\n[3] = Vedantu\n[4] = Back\n\n")
    if con1 == "1":
        time.sleep(2)
        webbrowser.open("https://dpspatna.com/")
        time.sleep(2)
        main()
    elif con1 == "2":
        time.sleep(2)
        webbrowser.open("https://byjus.com/")
        time.sleep(2)
        main()
    elif con1 == "3":
        time.sleep(2)
        webbrowser.open("https://vedantu.com/")
        time.sleep(2)
        main()
    elif con1 == "4":
        main()
    else:
        edu()

def main():
    os.system("CLS")
    webbrowser.Chrome(open("Suzie.png"))
    os.system("CLS")
    time.sleep(5)
    subprocess.call("TASKKILL /f  /IM  Microsoft.Photos.EXE")
    headn = head.center(20)
    print(headn)
    print()
    time.sleep(1)
    print("Options - \n[1] = Security\n[2] = Entertainment\n[3] = Education\n[4] = Exit")
    print()
    op = input("")
    if op == "1":
        sec()
    elif op == "2":
        ser()
    elif op == "3":
        edu()
    elif op == "4":
        time.sleep(2)
        print()
        os.system("CLS")
        print("Closing 'SUIZEN'.......")
        time.sleep(2)
        os.system("CLS")
        quit()
    else:
        os.system("CLS")
        print("Please Enter a Valid Digit !")
        time.sleep(3)
        main()
#Main Code Ends

#Execute the Main() Function to Start The Program
os.system("CLS")
print("Starting 'SUIZEN'.......")
time.sleep(4)
main()
