import tkinter as tk
import os.path
from os import path


#checking to see if files already exists
f_path = path.exists("front.txt") #checks for front.txt's path
b_path = path.exists("back.txt")#checks for back.txt's path

left_path = os.path.dirname(os.path.realpath('leftarrow.png')) + '\Downloads\Examhelp\SDEV140_Project-main\SDEV140_Project-main\\leftarrow.png'
right_path = os.path.dirname(os.path.realpath('rightarrow.png')) + '\Downloads\Examhelp\SDEV140_Project-main\SDEV140_Project-main\\rightarrow.png'
flip_path = os.path.dirname(os.path.realpath('flipimg.png')) + '\Downloads\Examhelp\SDEV140_Project-main\SDEV140_Project-main\\flipimg.png'
flash_path = os.path.dirname(os.path.realpath('flash.png')) + '\Downloads\Examhelp\SDEV140_Project-main\SDEV140_Project-main\\flash.png'
print(left_path)
if f_path and b_path: #checking for both
  pass
else:
  #creating two txt files to store front and back side of cards
  front = open('front.txt', 'w')
  back = open('back.txt', 'w')
  front.close()
  back.close()
#creating main window, title, and size
main = tk.Tk()
main.title("Examhelp Main Window")
main.geometry("300x300")

#text for showing App name
hello = tk.Label(text="Welcome to Examhelp!")
hello.pack()

#Creating delete function to remove all data from both front and back.txt
def delete():
  open("front.txt", "w").close()
  open("back.txt", "w").close()

#delete button
delete = tk.Button(main, text='Delete ALL cards', command=delete)
delete.place(x=100, y=150)

a = tk.PhotoImage(file = r"{}".format(left_path)) #variable to display left arrow image
b = tk.PhotoImage(file = r"{}".format(right_path))#variable to display right arrow image
c = tk.PhotoImage(file = r"{}".format(flip_path))#displaying flip image
d = tk.PhotoImage(file = r'{}'.format(flash_path))#displaying flashcard iamge in main
left = a.subsample(3, 3)
right = b.subsample(3, 3)
fl = c.subsample(5,5)
flash = d.subsample(3,3)

#Creating Question-making window
def q_win():
  q_win = tk.Toplevel()
  q_win.title("Question Window")
  q_win.geometry("300x300")
  main.withdraw()

  #creating labels for question window
  front_side = tk.Label(q_win, text='Front Side').place(x=120, y=5)
  back_side = tk.Label(q_win, text='Back Side').place(x=120, y=65)
  instructions = tk.Label(q_win, text= 'Enter any characters.\nCharacters can include letters, numbers, \nand special characters.\nAt least one box has to have an input'
  ).place(x=25, y=200)
  #creating text boxes of front side and back side for user input
  side_a = tk.Entry(q_win, font=('Arial', 13))
  side_a.place(x=50, y=30)
  side_b = tk.Entry(q_win, font=('Arial', 13))
  side_b.place(x=50, y=90)

  #back function removes question window and goes back to main menu
  def backquestion():
    main.deiconify()
    q_win.destroy()

  #function to save text and numbers into two txt files
  def save():
    if side_a.get() == '' and side_b.get() == '': #checking both boxes to see if they're empty
      no_input = tk.Label(q_win, text="Please place an input in at least ONE box", font=('Helvetica bold', 10), fg="red") #if there's no input on both boxes, it will display instructions
      no_input.place(x=15, y=175)
      q_win.after(3000, no_input.destroy) #destroys label after 3 seconds
    else:
      front = open('front.txt', 'a') # if there is an entry, it will open the two files
      back = open('back.txt', 'a')
      front.write(str(side_a.get()) + '\n') #appending inputs with a newline onto txt files
      back.write(str(side_b.get()) + '\n')
      front.close() #closing files
      back.close()
      side_a.delete(0, 'end') #clearing the entry boxes after saving
      side_b.delete(0, 'end')

  #Function to clear entry boxes before saving
  def clear():
    side_a.delete(0, 'end')
    side_b.delete(0, 'end')

  #creating all the buttons for saving, clearing, and going back from the question window
  q_back = tk.Button(q_win, text="Back", command=backquestion).place(x=125, y=270)
  save = tk.Button(q_win, text="Save", command=save).place(x=125, y=135)
  clear = tk.Button(q_win, text="Clear", command=clear).place(x=225, y=135)
  
#Keeping track of which card user is on
page = 0

#Creating testing window
def t_win():
  t_win = tk.Toplevel()
  t_win.title("Testing Window")
  t_win.geometry("300x300")
  main.withdraw()
  #Putting text on card
  text = tk.Text(t_win, height=9, width=35)
  text.tag_configure("center", justify='center')
  text.tag_add("center", "0.0", "end")
  text.place(x=7, y=40)
  t_win.resizable(False, False)

  #Making label for card number with 1 as starting point for aesthetic reasons
  card_num = tk.Label(t_win, text=f"Card #{page+1}")
  card_num.place(x=210, y=17)

  #showing the front side of the card when user clicks test mode
  front = open('front.txt', 'r')
  lines = front.readlines()
  try: #making sure error is ignored when user clicks test mode without any inputs
    text.insert('0.0', '\n\n\n' + lines[page]) #inserting the front-side input based on the page
    text.tag_add("center", "0.0", "end")
    text.update()
    front.close()
  except Exception: #passing error
    pass

  #function meant to switch the card to the back side
  def flip():
    global flip_num
    if flip_num == 0: #flipping card from front to back
      flip_num = 1
      back = open('back.txt', 'r')
      lines = back.readlines()
      text.delete("0.0", "end")
      try: #bypassing error if there's an invalid index
        text.insert('0.0', '\n\n\n' + lines[page]) #inserting back-side of inputs
        text.tag_add("center", "0.0", "end")
        text.update()
      except Exception:
        pass
      back.close()
      text.update()
    else:
      flip_num = 0 # Card swtiches from back to front
      front = open('front.txt', 'r')
      lines = front.readlines()
      text.delete("0.0", "end")
      try:
        text.insert('0.0', '\n\n\n' + lines[page]) #inserting front side of inputs after flipping
        text.tag_add("center", "0.0", "end")
        text.update()
      except Exception:
        pass
      front.close()

  #creating button for flip command
  global fl
  flip_button = tk.Button(t_win, text="Flip",image=fl, command=flip)
  flip_button.place(x=120, y=200)

  #function to go on to the next card or set of questions
  def forwards():
    global page
    page += 1 #adding to page to increase index of front/back.txt
    front = open('front.txt', 'r')
    if page > 0:# enables previous button in order to go back once user goes forward a page
      previous['state'] = 'normal'
    if page == len(lines) - 1: #disables forward button once it reaches end of cards
      forward['state'] = 'disabled'
    text.delete("0.0", "end")
    text.insert('0.0', '\n\n\n' + lines[(page)])
    text.tag_add("center", "0.0", "end")
    card_num['text'] = f"Card #{page+1}" #updating card number with each click
    text.update()
    front.close()

  #Button to go to the previous card/ set of questions
  def backwards():
    global page
    page -= 1 #decreasing page value by one
    front = open('front.txt', 'r')
    back = open('back.txt', 'r')
    f_lines = front.readlines()
    b_lines = back.readlines()
    if page <= 0: #disables 'previous' button at the beginning
      previous['state'] = 'disabled'
    elif page == len(f_lines) - 2: 
      forward['state'] = 'normal'
    if page == 0 and len(f_lines) == 2 and len(b_lines) == 2: #checks to see if there are two questions so that the forward button isn't disabled by "page == len(lines) - 1"
      forward['state'] = 'normal'
    text.delete("0.0", "end")
    text.insert('0.0', '\n\n\n' + lines[(page)])
    text.tag_add("center", "0.0", "end")
    card_num['text'] = f"Card #{page+1}" #updating card number
    text.update()
    front.close()

  
  #creating forwards and previous buttons
  forward = tk.Button(t_win, text="Forward >", image=right, command=forwards)
  forward.place(x=215, y=200)
  previous = tk.Button(t_win, text="< Previous", command=backwards, image=left, state='disabled')
  previous.place(x=24, y=200)
  front = open('front.txt', 'r')
  back = open('back.txt', 'r')
  f_lines = front.readlines()
  b_lines = back.readlines()
  if len(f_lines) < 1 and len(b_lines) < 1: #if there's 0 questions, forward button is disabled since there's nothing ahead and message will appear
    forward['state'] = 'disabled'
    none = tk.Label(t_win, text="Please go to the 'question' menu to create \na question", font=('Helvetica bold', 10), fg="red")
    none.place(x=15, y=230)
    t_win.after(3000, none.destroy)
  if len(f_lines) == 1 and len(b_lines) == 1: #if there's only one question, forward button is dissabled. This was mostly a hard-coded bug fix
    forward['state'] = 'disabled'
  if len(f_lines) > 2 and len(b_lines) > 2: #if there's more than 2 questions, the forward button is activated
    forward['state'] = 'normal'
  front.close()
  back.close()

  #back button function for test window
  def backtest():
    main.deiconify()
    t_win.destroy()

  #creating back button
  t_back = tk.Button(t_win, text="Back", command=backtest).place(x=125, y=270)

#number to determine which side card/ question is on
flip_num = 0


#Making buttons to access question window and test window
questions = tk.Button(main, text="Question mode", width=12, command=q_win)
questions.pack()
test = tk.Button(main, text="Test Mode", width=12, command=t_win)
test.pack()
flashimg = tk.Button(main, text='Flashcard', image = flash) #non-functional button. Purely for image display
flashimg.pack()
#Creating an exit button for user to quit main window
def exit():
  main.destroy()

#exit button
exit = tk.Button(main, text="Exit", command=exit)
exit.place(x=125, y=270)

tk.mainloop()
