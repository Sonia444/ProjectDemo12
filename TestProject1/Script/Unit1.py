def Test1():
    #Runs the "Orders" tested application.
    TestedApps.Orders.Run()
    #Moves the mouse cursor to the menu item specified and then simulates a single click.
    Aliases.Orders.MainForm.MainMenu.Click("Orders|New order...")
    #Clicks the 'Customer' object.
    Aliases.Orders.OrderForm.Group.Customer.Click(70, 7)
    #Enters '[Caps]' in the 'Customer' object.
    Aliases.Orders.OrderForm.Group.Customer.Keys("[Caps]")
    #Enters the text 'S' in the 'Customer' text editor.
    Aliases.Orders.OrderForm.Group.Customer.SetText("S")
    #Enters '[Caps]' in the 'Customer' object.
    Aliases.Orders.OrderForm.Group.Customer.Keys("[Caps]")
    #Enters the text 'Sonia' in the 'Customer' text editor.
    Aliases.Orders.OrderForm.Group.Customer.SetText("Sonia")
    #Clicks the 'Street' object.
    Aliases.Orders.OrderForm.Group.Street.Click(60, 8)
    #Clicks the 'Street' object.
    Aliases.Orders.OrderForm.Group.Street.Click(81, 15)
    #Enters the text 'str1' in the 'Street' text editor.
    Aliases.Orders.OrderForm.Group.Street.SetText("str1")
    #Clicks the 'City' object.
    Aliases.Orders.OrderForm.Group.City.Click(100, 4)
    #Enters the text 'tpg' in the 'City' text editor.
    Aliases.Orders.OrderForm.Group.City.SetText("tpg")
    #Clicks the 'State' object.
    Aliases.Orders.OrderForm.Group.State.Click(50, 7)
    #Enters '![ReleaseLast][Caps]' in the 'State' object.
    Aliases.Orders.OrderForm.Group.State.Keys("![ReleaseLast][Caps]")
    #Enters the text 'A' in the 'State' text editor.
    Aliases.Orders.OrderForm.Group.State.SetText("A")
    #Enters '[Caps]' in the 'State' object.
    Aliases.Orders.OrderForm.Group.State.Keys("[Caps]")
    #Enters the text 'Ap' in the 'State' text editor.
    Aliases.Orders.OrderForm.Group.State.SetText("Ap")
    #Clicks the 'Zip' object.
    Aliases.Orders.OrderForm.Group.Zip.Click(9, 5)
    #Enters the text '543367' in the 'Zip' text editor.
    Aliases.Orders.OrderForm.Group.Zip.SetText("543367")
    #Clicks the 'CardNo' object.
    Aliases.Orders.OrderForm.Group.CardNo.Click(92, 8)
    #Enters the text '56787890' in the 'CardNo' text editor.
    Aliases.Orders.OrderForm.Group.CardNo.SetText("56787890")
    #Clicks the 'ButtonOK' button.
    Aliases.Orders.OrderForm.ButtonOK.ClickButton()
    #Clicks the 'MainForm' object.
    Aliases.Orders.MainForm.Click(67, 43)
    #Moves the mouse cursor to the menu item specified and then simulates a single click.
    Aliases.Orders.MainForm.MainMenu.Click("Orders|New order...")
    #Clicks the 'Customer' object.
    Aliases.Orders.OrderForm.Group.Customer.Click(48, 1)
    #Clicks the 'Customer' object.
    Aliases.Orders.OrderForm.Group.Customer.Click(51, 19)
    #Clicks the 'Customer' object.
    Aliases.Orders.OrderForm.Group.Customer.Click(40, 11)
    #Enters the text 'sty' in the 'Customer' text editor.
    Aliases.Orders.OrderForm.Group.Customer.SetText("sty")
    #Clicks the 'Street' object.
    Aliases.Orders.OrderForm.Group.Street.Click(44, 6)
    #Enters the text 'srr1' in the 'Street' text editor.
    Aliases.Orders.OrderForm.Group.Street.SetText("srr1")
    #Clicks the 'City' object.
    Aliases.Orders.OrderForm.Group.City.Click(91, 7)
    #Enters the text 'hyd' in the 'City' text editor.
    Aliases.Orders.OrderForm.Group.City.SetText("hyd")
    #Clicks the 'State' object.
    Aliases.Orders.OrderForm.Group.State.Click(115, 7)
    #Enters the text 'ts' in the 'State' text editor.
    Aliases.Orders.OrderForm.Group.State.SetText("ts")
    #Clicks the 'Zip' object.
    Aliases.Orders.OrderForm.Group.Zip.Click(62, 15)
    #Enters the text '65647' in the 'Zip' text editor.
    Aliases.Orders.OrderForm.Group.Zip.SetText("65647")
    #Clicks the 'CardNo' object.
    Aliases.Orders.OrderForm.Group.CardNo.Click(87, 10)
    #Enters the text '87655567' in the 'CardNo' text editor.
    Aliases.Orders.OrderForm.Group.CardNo.SetText("87655567")
    #Clicks the 'ButtonOK' button.
    Aliases.Orders.OrderForm.ButtonOK.ClickButton()
    #Moves the mouse cursor to the menu item specified and then simulates a single click.
    Aliases.Orders.MainForm.MainMenu.Click("Orders|New order...")
    #Selects the 'ScreenSaver' item of the 'ProductNames' combo box.
    Aliases.Orders.OrderForm.Group.ProductNames.ClickItem("ScreenSaver")
    #Clicks the 'Customer' object.
    Aliases.Orders.OrderForm.Group.Customer.Click(73, 13)
    #Clicks the 'ButtonCancel' button.
    Aliases.Orders.OrderForm.ButtonCancel.ClickButton()
    #Double-clicks the 0 subitem of the 'sty' item of the 'OrdersView' list view.
    Aliases.Orders.MainForm.OrdersView.DblClickItem("sty")
    #Selects the 'ScreenSaver' item of the 'ProductNames' combo box.
    Aliases.Orders.OrderForm.Group.ProductNames.ClickItem("ScreenSaver")
    #Clicks the 'Customer' object.
    Aliases.Orders.OrderForm.Group.Customer.Click(73, 10)
    #Enters the text 'parimi' in the 'Customer' text editor.
    Aliases.Orders.OrderForm.Group.Customer.SetText("parimi")
    #Clicks the 'ButtonOK' button.
    Aliases.Orders.OrderForm.ButtonOK.ClickButton()
    #Double-clicks the 0 subitem of the 'Sonia' item of the 'OrdersView' list view.
    Aliases.Orders.MainForm.OrdersView.DblClickItem("Sonia")
    #Clicks the 'ButtonCancel' button.
    Aliases.Orders.OrderForm.ButtonCancel.ClickButton()
    #Moves the mouse cursor to the menu item specified and then simulates a single click.
    Aliases.Orders.MainForm.MainMenu.Click("Orders|Delete order")
    #Clicks the 'btnYes' button.
    Aliases.Orders.dlgConfirmation.btnYes.ClickButton()
    #Closes the 'MainForm' window.
    Aliases.Orders.MainForm.Close()
    #Clicks the 'btnNo' button.
    Aliases.Orders.dlgConfirmation.btnNo.ClickButton()
