### **Description:**

This is a project to manage a small sales business.

The one who interacts with the page is the user, that is, the one who works on the premises.

You can register products, categories, customers, and of course sales recorder.

On the home page are the graphs with the sales statistics by year and by month.

### **Implementation:**

It's made in Django, now it uses sqlite, but it can be changed for postgres or mySQL. On the frontend I use AdminLte3 to
layout and styles, I use jQuery to handle events and do other functionalities, practically all the frontend
it is made with jQuery and pure JavaScript, except for Django Templates as a template language which I use for
make my base templates, inherit from them, request forms and other data from the server.

I also use many plugins like datatable, datepicker, jqueryUI, select2, etc.

I use a view based on TemplateView classes and through requests with ajax on the frontend, I manage the CRUDs and do all the
operations on the same page without updating it.

It would be missing the part of the users, the login and the sending of emails, also other functionalities such as printing pdf.
