import requests
import tkinter

# data = requests.get("https://api.kanye.rest")
# '''
# api-key: https://api.kanye.rest
# form:https://kanye.rest/
# data obtained from api using get() method is need to be 
# converted into json format.
# '''
# data_in_json = data.json()
# # print(data_in_json)
# quote = data_in_json['quote']
# # print(quote)

def change_quote():
    data = requests.get("https://api.kanye.rest")
    data_in_json = data.json()
    quote = data_in_json['quote']
    canvas.itemconfig(quote_text,text = quote)

    

window = tkinter.Tk()
window.title('kanye says...')
window.config(padx=30,pady=30)
canvas = tkinter.Canvas(height=400,width=300)
background = tkinter.PhotoImage(file='background.png')
canvas.create_image(150,200, image=background)

canvas.grid(row=0,column=0)

kanye_image = tkinter.PhotoImage(file="kanye.png")
# canvas.create_image(240,500,image = kanye_image)
kanye_button = tkinter.Button(image=kanye_image,command=change_quote)
kanye_button.grid(row=1,column=0)

quote_text = canvas.create_text(160,170,width=200, text="hello",fill="white", font=("Arial", 20,"normal"))
window.mainloop()