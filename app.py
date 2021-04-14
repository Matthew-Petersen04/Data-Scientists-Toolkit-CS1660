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
    
def open_markdown():
    wb.open_new('http://host.docker.internal:12345/')


root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

RStudioButton = tk.Button(frame,
                   text="RStudio",
                   command=open_rstudio)
RStudioButton.pack(side = tk.TOP)

SpyderButton = tk.Button(frame,
                   text="Spyder",
                   command=open_spyder)
SpyderButton.pack(side = tk.TOP)

IBMSASButton = tk.Button(frame,
                   text="IBM SAS",
                   command=open_rstudio)
IBMSASButton.pack(side = tk.TOP)

GitBucketButton = tk.Button(frame,
                   text="GitBucket",
                   command=open_gitbucket)
GitBucketButton.pack(side = tk.TOP)

JupyterButton = tk.Button(frame,
                        text="Jupyter Notebook",
                        command=open_jupyter)
JupyterButton.pack(side = tk.TOP)

OrangeButton = tk.Button(frame,
                        text="Orange",
                        command=open_jupyter)
OrangeButton.pack(side = tk.TOP)

VisualStudioButton = tk.Button(frame,
                        text="Visual Studio Code IDE",
                        command=open_vs)
VisualStudioButton.pack(side = tk.TOP)

HadoopButton = tk.Button(frame,
                        text="Apache Hadoop",
                        command=open_jupyter)
HadoopButton.pack(side = tk.TOP)

SparkButton = tk.Button(frame,
                        text="Apache Spark",
                        command=open_jupyter)
SparkButton.pack(side = tk.TOP)

TableauButton = tk.Button(frame,
                        text="Tableau",
                        command=open_jupyter)
TableauButton.pack(side = tk.TOP)

SonarButton = tk.Button(frame,
                        text="SonarCloud",
                        command=open_jupyter)
SonarButton.pack(side = tk.TOP)

TensorflowButton = tk.Button(frame,
                        text="Tensorflow",
                        command=open_jupyter)
TensorflowButton.pack(side = tk.TOP)

MarkdownButton = tk.Button(frame,
                        text="Markdown",
                        command=open_markdown)
MarkdownButton.pack(side = tk.TOP)


root.mainloop()