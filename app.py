import tkinter as tk
import webbrowser as wb
    

def open_rstudio():
    wb.open_new('http://host.docker.internal:8787/')
    
def open_vs():
    wb.open_new('http://host.docker.internal:6080/vnc.html')
    
def open_gitbucket():
    wb.open_new('http://host.docker.internal:8080/')
    
def open_jupyter():
    wb.open_new('http://host.docker.internal:8888/')
    
def open_spyder():
    wb.open_new('http://host.docker.internal:6081/vnc.html')

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

RStudioButton = tk.Button(frame,
                   text="RStudio",
                   command=open_rstudio)
RStudioButton.pack(side = tk.TOP)

RStudioButton = tk.Button(frame,
                   text="Spyder",
                   command=open_spyder)
RStudioButton.pack(side = tk.TOP)

RStudioButton = tk.Button(frame,
                   text="IBM SAS",
                   command=open_rstudio)
RStudioButton.pack(side = tk.TOP)

RStudioButton = tk.Button(frame,
                   text="GitBucket",
                   command=open_gitbucket)
RStudioButton.pack(side = tk.TOP)

VisualStudioButton = tk.Button(frame,
                        text="Jupyter Notebook",
                        command=open_jupyter)
VisualStudioButton.pack(side = tk.TOP)

VisualStudioButton = tk.Button(frame,
                        text="Orange",
                        command=open_jupyter)
VisualStudioButton.pack(side = tk.TOP)

VisualStudioButton = tk.Button(frame,
                        text="Visual Studio Code IDE",
                        command=open_vs)
VisualStudioButton.pack(side = tk.TOP)

VisualStudioButton = tk.Button(frame,
                        text="Apache Hadoop",
                        command=open_jupyter)
VisualStudioButton.pack(side = tk.TOP)

VisualStudioButton = tk.Button(frame,
                        text="Apache Spark",
                        command=open_jupyter)
VisualStudioButton.pack(side = tk.TOP)

VisualStudioButton = tk.Button(frame,
                        text="Tableau",
                        command=open_jupyter)
VisualStudioButton.pack(side = tk.TOP)

VisualStudioButton = tk.Button(frame,
                        text="SonarCloud",
                        command=open_jupyter)
VisualStudioButton.pack(side = tk.TOP)

VisualStudioButton = tk.Button(frame,
                        text="Tensorflow",
                        command=open_jupyter)
VisualStudioButton.pack(side = tk.TOP)

VisualStudioButton = tk.Button(frame,
                        text="Markdown",
                        command=open_jupyter)
VisualStudioButton.pack(side = tk.TOP)


root.mainloop()