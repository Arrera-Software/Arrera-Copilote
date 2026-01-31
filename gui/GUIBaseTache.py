from tkinter.messagebox import showerror, askyesno, showinfo
from tkcalendar import Calendar
from fnc.fonctionTache import fncArreraTache
from gui.guibase import GuiBase,gestionnaire
import tkinter as tk
from datetime import datetime,date
from functools import partial

class GUIBaseTache(GuiBase):
    def __init__(self, gestionnaire: gestionnaire,fncTask:fncArreraTache):
        super().__init__(gestionnaire,"Tache")
        self._fnctask = fncTask
        self.__directoryAsset = self._gestionnaire.getConfigFile().asset+"tache/"
        self._title = ""

    def _mainframe(self):
        self._screen.title(self._title)
        # Var
        self.__varAddDescription = tk.BooleanVar(value=False)
        self.__varAddDate = tk.BooleanVar(value=False)
        # Frame
        frameTitle = self._arrtk.createFrame(self._screen)
        self.__frameTask = self._arrtk.createFrame(self._screen)
        self.__frameAdd = self._arrtk.createFrame(self._screen)
        self.__frameAddTask = self._arrtk.createFrame(self.__frameAdd)
        frameBTNAdd = self._arrtk.createFrame(self.__frameAddTask)
        self.__frameSuppression = self._arrtk.createFrame(self._screen)
        self.__frameSuppr = self._arrtk.createFrame(self.__frameSuppression)


        # Config

        self.__frameAdd.rowconfigure(0, weight=1)
        self.__frameAdd.columnconfigure(0, weight=1)

        self.__frameAddTask.columnconfigure(0, weight=1)
        self.__frameAddTask.rowconfigure(4, weight=1)

        frameBTNAdd.columnconfigure(0, weight=1)
        frameBTNAdd.columnconfigure(1, weight=1)

        self.__frameSuppression.grid_columnconfigure(0, weight=1)
        self.__frameSuppression.grid_rowconfigure(1, weight=1)

        # img
        imgLogo = self._arrtk.createImage(pathLight=self.__directoryAsset+"task.png",
                                          pathDark=self.__directoryAsset+"task.png",
                                          tailleX=64, tailleY=64)
        imgSuppr = self._arrtk.createImage(pathLight=self.__directoryAsset+"task-suppr.png",
                                          pathDark=self.__directoryAsset+"task-suppr.png",
                                            tailleX=32, tailleY=32)
        imgPlus = self._arrtk.createImage(pathLight=self.__directoryAsset+"task-plus.png",
                                           pathDark=self.__directoryAsset+"task-plus.png",
                                           tailleX=32, tailleY=32)

        self.__imgNoFinish = self._arrtk.createImage(pathLight=self.__directoryAsset+"task-nofinish.png",
                                                     pathDark=self.__directoryAsset+"task-nofinish.png",
                                                     tailleX=32, tailleY=32)

        self.__imgFinish = self._arrtk.createImage(pathLight=self.__directoryAsset+"task-finish.png",
                                                     pathDark=self.__directoryAsset+"task-finish.png",
                                                     tailleX=32, tailleY=32)
        # Widgets
        labelLogo = self._arrtk.createLabel(frameTitle,text="",image=imgLogo)
        labelTitle = self._arrtk.createLabel(frameTitle,text=self._title,
                                             ppolice="Arial",ptaille=20,pstyle="bold")
        btnAddTask = self._arrtk.createButton(frameTitle,text="",image=imgPlus,command=self.__viewAddTask
                                              ,bg=self._btnColor,fg=self._btnTexteColor)
        btnDelTask = self._arrtk.createButton(frameTitle,text="",image=imgSuppr,command=self.__viewSuppr
                                              ,bg=self._btnColor,fg=self._btnTexteColor)
        self.__btnFinishTask = self._arrtk.createButton(frameTitle,text="",image=self.__imgFinish
                                                        ,bg=self._btnColor,fg=self._btnTexteColor)

        # Add task frame
        # Add
        labelTitleAddTask = self._arrtk.createLabel(self.__frameAddTask, text="Ajouter une tâche",
                                                    ppolice="Arial", ptaille=35, pstyle="bold")
        widgetName,self.__entryNameTask = self._arrtk.createEntryLegend(self.__frameAddTask, text="Nom de la tache : ", ppolice="Arial",
                                                                        ptaille=20, gridUsed=True)

        self.__calendarDate = Calendar(self.__frameAddTask,selectmode="day",year=date.today().year,
                                       month=date.today().month,locale="fr_FR",firstweekday="monday",
                                       showweeknumbers=False,borderwidth=0)
        wDescription,self.__entryDescriptionTask = self._arrtk.createEntryLegend(self.__frameAddTask, text="Description : ", ppolice="Arial",
                                                     ptaille=20, gridUsed=True)

        btnCancelAddTask = self._arrtk.createButton(frameBTNAdd,text="Annuler",command=self.__backToMain
                                                    ,bg=self._btnColor,fg=self._btnTexteColor,
                                                    ppolice="Arial", ptaille=25,pstyle="bold")
        btnConfirmAddTask = self._arrtk.createButton(frameBTNAdd, text="Confirmer", command=self.__addNewTask
                                                     ,bg=self._btnColor,fg=self._btnTexteColor,
                                                     ppolice="Arial", ptaille=25,pstyle="bold")

        # Supp
        labelTitleSuppr = self._arrtk.createLabel(self.__frameSuppression, text="Supprimer une tâche",
                                                  ppolice="Arial", ptaille=35, pstyle="bold")
        btnBackSuppr = self._arrtk.createButton(self.__frameSuppression, text="Retourner a l'acceuil",
                                                command=self.__backToMain,bg=self._btnColor,fg=self._btnTexteColor,
                                                ppolice="Arial", ptaille=25,pstyle="bold")

        # Placement
        # Widget
        labelLogo.pack(side="left", padx=(10, 5))
        labelTitle.pack(side="left", padx=(5, 10))
        self.__btnFinishTask.pack(side="right", padx=(5, 10))
        btnDelTask.pack(side="right", padx=(5, 10))
        btnAddTask.pack(side="right", padx=(10, 5))

        labelTitleAddTask.grid(row=0, column=0, sticky="n", pady=(10, 8))
        widgetName.grid(row=1, column=0, sticky="ew", padx=10, pady=(2, 8))
        self.__calendarDate.grid(row=2, column=0, sticky="", padx=10, pady=(0, 8))
        wDescription.grid(row=3, column=0, sticky="ew", padx=10, pady=(0, 8))

        frameBTNAdd.grid(row=5, column=0, sticky="ew", padx=10, pady=(8, 10))

        btnCancelAddTask.grid(row=0, column=0, sticky="w", padx=(0, 5))
        btnConfirmAddTask.grid(row=0, column=1, sticky="e", padx=(5, 0))

        labelTitleSuppr.grid(row=0, column=0, sticky="ew")
        self.__frameSuppr.grid(row=1, column=0, sticky="nsew")
        btnBackSuppr.grid(row=2, column=0, sticky="ew")

        # Frame
        frameTitle.pack(side="top", fill="x", pady=(0, 2))
        self.__frameTask.pack(side="top", fill="both", expand=True, pady=(2, 2))
        self.__viewTaskNoFinish()

    def __disableAllFrame(self):
        self.__frameTask.pack_forget()
        self.__frameAdd.pack_forget()
        self.__frameSuppression.pack_forget()
        self._screen.update()

    def __viewTaskNoFinish(self):
        self.__disableAllFrame()
        self.__frameTask.pack(side="top", fill="both", expand=True, pady=(2, 2))
        # ta liste de tâches
        tasks = self._fnctask.getNoFinishTask()

        self.__btnFinishTask.configure(text="",image=self.__imgFinish,
                                       command=self.__viewTaskFinish)

        # 1) nettoyer le frame si déjà utilisé
        for w in self.__frameTask.winfo_children():
            w.destroy()

        # 2) faire en sorte que le frame parent grandisse correctement
        self.__frameTask.grid_rowconfigure(0, weight=1)
        self.__frameTask.grid_columnconfigure(0, weight=1)

        # 3) un unique conteneur scrollable, toujours
        if len(tasks) != 0:
            container = self._arrtk.createScrollFrame(self.__frameTask,bg="transparent")
            container.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

            # 4) les colonnes du conteneur prennent la largeur
            container.grid_columnconfigure(0, weight=1)

            # 5) créer les checkboxes
            self._task_vars = []  # pour relire l'état plus tard
            for i, label in enumerate(tasks):
                var = tk.BooleanVar(value=False)
                cb = self._arrtk.createCheckbox(container, text=label,
                                                var_chk=var,
                                                command= partial (self.__finishTask,var, label))
                cb.grid(row=i, column=0, sticky="w", padx=8, pady=(0, 4))
                self._task_vars.append(var)
        else:
            labelNoTask = self._arrtk.createLabel(self.__frameTask,text="Aucune tâche pour le moment",
                                                  ppolice="Arial",ptaille=40,pstyle="bold")
            labelNoTask.pack(pady=20)

        self._screen.update()

    def __finishTask(self, var:tk.BooleanVar, name:str):
        if var.get():
            self._fnctask.finishTask(name)
            self.__viewTaskNoFinish()

    def __viewTaskFinish(self):
        self.__disableAllFrame()
        self.__frameTask.pack(side="top", fill="both", expand=True, pady=(2, 2))
        # ta liste de tâches
        tasks = self._fnctask.getFinishTask()

        self.__btnFinishTask.configure(text="",image=self.__imgNoFinish,
                                       command=self.__viewTaskNoFinish)

        # 1) nettoyer le frame si déjà utilisé
        for w in self.__frameTask.winfo_children():
            w.destroy()

        # 2) faire en sorte que le frame parent grandisse correctement
        self.__frameTask.grid_rowconfigure(0, weight=1)
        self.__frameTask.grid_columnconfigure(0, weight=1)

        # 3) un unique conteneur scrollable, toujours
        if len(tasks) != 0:
            container = self._arrtk.createScrollFrame(self.__frameTask,bg="transparent")
            container.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

            # 4) les colonnes du conteneur prennent la largeur
            container.grid_columnconfigure(0, weight=1)

            # 5) créer les checkboxes
            self._task_vars = []  # pour relire l'état plus tard
            for i, label in enumerate(tasks):
                var = tk.BooleanVar(value=True)
                cb = self._arrtk.createCheckbox(container, text=label,
                                                var_chk=var,
                                                command=partial(self.__unfinishTask, var, label))
                cb.grid(row=i, column=0, sticky="w", padx=8, pady=(0, 4))
                self._task_vars.append(var)
        else:
            labelNoTask = self._arrtk.createLabel(self.__frameTask,text="Aucune tâche fini pour le moment",
                                                  ppolice="Arial",ptaille=40,pstyle="bold")
            labelNoTask.pack(pady=20)

        self._screen.update()

    def __unfinishTask(self, var:tk.BooleanVar, name:str):
        if not var.get():
            self._fnctask.unfinishTask(name)
            self.__viewTaskFinish()

    def __viewAddTask(self):
        self.__disableAllFrame()
        self.__varAddDate.set(False)
        self.__varAddDescription.set(False)
        self.__entryNameTask.delete(0, tk.END)
        self.__frameAdd.pack(side="top", fill="both", expand=True, pady=(2, 2))
        self.__frameAddTask.grid(row=0, column=0, sticky="nsew")
        self._screen.update()

    def __addNewTask(self):
        # Var
        dateAdd = False
        descriptionAdd = False

        name = self.__entryNameTask.get()
        if name == "":
            showerror("Erreur",
                      "Le nom de la tâche ne peut pas être vide")
            return

        dateCalendar = self.__calendarDate.selection_get()

        if dateCalendar:
            self.__calendarDate.selection_clear()
            dateAdd = True

        description = self.__entryDescriptionTask.get()
        if description != "":
            descriptionAdd = True
            self.__entryDescriptionTask.delete(0, tk.END)

        if dateAdd and not descriptionAdd:
            if not self._fnctask.addTask(name,date=dateCalendar):
                showerror("Erreur","La tache n'a pas pu être ajouter")
        elif dateAdd and descriptionAdd:
            if not self._fnctask.addTask(name,date=dateCalendar,description=description):
                showerror("Erreur","La tache n'a pas pu être ajouter")
        elif not dateAdd and descriptionAdd:
            if not self._fnctask.addTask(name,description=description):
                showerror("Erreur","La tache n'a pas pu être ajouter")
        else :
            if not self._fnctask.addTask(name):
                showerror("Erreur","La tache n'a pas pu être ajouter")

        self.__viewTaskNoFinish()

    def __backToMain(self):
        self.__frameAdd.grid_forget()
        self.__frameSuppression.pack_forget()
        self.__frameTask.pack(side="top", fill="both", expand=True, pady=(2, 2))
        self._screen.update()
        self.__viewTaskNoFinish()

    def __viewSuppr(self):
        self.__disableAllFrame()
        self.__frameSuppression.pack(side="top", fill="both", expand=True, pady=(2, 2))

        # ta liste de tâches
        tasks = self._fnctask.getAllTask()

        # 1) nettoyer le frame si déjà utilisé
        for w in self.__frameSuppr.winfo_children():
            w.destroy()

        # 2) faire en sorte que le frame parent grandisse correctement
        self.__frameSuppr.grid_rowconfigure(0, weight=1)
        self.__frameSuppr.grid_columnconfigure(0, weight=1)

        # 3) un unique conteneur scrollable, toujours
        if len(tasks) != 0:
            container = self._arrtk.createScrollFrame(self.__frameSuppr,bg="transparent")
            container.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

            # 4) les colonnes du conteneur prennent la largeur
            container.grid_columnconfigure(0, weight=1)

            # 5) créer les checkboxes
            self._task_vars = []  # pour relire l'état plus tard
            for i, label in enumerate(tasks):
                var = tk.BooleanVar(value=False)
                cb = self._arrtk.createCheckbox(container, text=label,
                                                var_chk=var,
                                                command= partial(self.__delTask,var, label))
                cb.grid(row=i, column=0, sticky="w", padx=8, pady=(0, 4))
                self._task_vars.append(var)
        else:
            labelNoTask = self._arrtk.createLabel(self.__frameSuppr,text="Aucune tâche enregistré",
                                                  ppolice="Arial",ptaille=40,pstyle="bold")
            labelNoTask.pack(pady=20)

        self._screen.update()

    def __delTask(self,var, name:str):
        if var.get():
            if (askyesno("Confirmation",
                         "Voulez vous vraiment supprimer cette tâche ?")):
                self._fnctask.delTask(name)
                showinfo("Tache","Suppression de la tâche effectué")
            self.__backToMain()
            self.__viewTaskNoFinish()

    def activeDel(self):
        self.active()
        self.__viewSuppr()

    def activeFinish(self):
        self.active()
        self.__viewTaskFinish()

    def activeAdd(self):
        self.active()
        self.__viewAddTask()