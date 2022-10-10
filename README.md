## [Mrs Naidu's Page](https://nighthawkcodingsociety.com/projectsearch/details/Flask%20Portfolio%20Starter)
Runtime link: https://portfolio.nighthawkcodingsociety.com/
### Idea
Starter code should be fun and practical.
### Visual thoughts
#### Organize with Bootstrap menu 
#### Add some color and fun through VANTA Visuals (birds, halo, solar, net)
#### Show some practical and fun links (hrefs) like Twitter, Git, Youtube
#### Show project specific links (hrefs) per page

### Implementation progress (August 13th, 2021)
#### Project entry point is main.py, this enables Flask Web App and provides capability to renders templates (HTML files)
#### The main.py is the  Web Server Gateway Interface, essentially it contains a HTTP route and HTML file relationship.  The Python code constructs WSGI relationships for index, kangaroos, walruses, and hawkers.
#### The project structure contains many directories and files.  The template directory (containing html files) and static directory (containing js files) are common standards for HTML coding.  Static files can be pictures and videos, in this project they are mostly javascript backgrounds.
#### WSGI templates: index.html, kangaroos.html, ... are aligned with routes in main.py.
#### Other templates support WSGI templates.  The base.html template contains common Head, Style, Body, Script definitions.  WSGI templates often "include" or "extend" these templates.  This is a way to reuse code.
#### The VANTA javascript statics (backgrounds) are shown and defaulted in base.html (birds), but are block replaced as needed in other templates (solar, net, ...)
#### The Bootstrap Navbar code is in navbar.html. The base.html code includes navbar.html.  The WSGI html files extend base.html files.  This is a process of management and correlation to optimize code management.  For instance, if the menu changes discovery of navbar.html is easy, one change reflects on all WSGI html files. 
#### The base.html uses combination of Bootstrap grid styling and custom CSS styling.  Grid styling in observe with the "<Col-3>" markers.  A Bootstrap Grid has a width of 12, thus four "Col-3" markers could fit on a Grid row.
#### A key purpose of this project is to embed links to other content.  The "href=" definition embeds hyperlinks into the rendered HTML.  The base.html file shows usage of "href={{github}}", the "{{github}}" is a Jinja2 variable.  Jinja2 variables are pre-processed by Python, a variable swap with value, before being sent to the browser.

### IDE management (things that happened beyond plan)
#### Recall on ".gitignore" solution to the pains of temporary files.  Start a ".gitignore" and avoid promoting temporary files to Git, for instance IDE xml files.
#### A project needs to establish a "requirements.txt" to keep track of Python packages used by the project.  This help in other IDEs and Deployment.  IntelliJ has menu Tool -> Sync Python Requirements to start file. 
  # My daily activities

<table>
   <tr>
    <th>Week</th>
    <th>Dates</th>
    <th>Subject</th>
    <th>Activity</th>
    <th>Activity</th>
    <th>Activity</th>
   </tr>
   
   <tr>
    <td></td>
    <td></td>
    <td> </td>
    <td></td>
    <td></td>
    <td></td>
   </tr>
   
   <tr>
    <td></td>
    <td></td>
    <td> </td>
    <td></td>
    <td></td>
    <td></td>
   </tr>
   
   <tr>
    <td></td>
    <td></td>
    <td> </td>
    <td></td>
    <td></td>
    <td></td>
   </tr>
    <tr>
    <td></td>
    <td></td>
    <td> </td>
    <td></td>
    <td></td>
    <td></td>
   </tr>
    <tr>
    <td></td>
    <td></td>
    <td> </td>
    <td></td>
    <td></td>
    <td></td>
   </tr>
   
   
  <tr>
    <td>1</td>
    <td>SCSS, Async</td>
    <td><a href="https://apclassroom.collegeboard.org/103/home?unit=1">1.3,1.4</a></td>
    <td><a href="https://github.com/nighthawkcoders/nighthawk_csp/wiki/Tri-2:-Tech-Talk-Week-1:-Organizing--Bootstrap-Files,-Templates-layouts,-and-Sassy">TT1.1, </a><a href="https://github.com/nighthawkcoders/nighthawk_csp/wiki/Tri-2:-Tech-Talk-Week-1:-Accessing-data-Asynchronously">TT1.2</a></td>
    <td><a href="https://poway.instructure.com/courses/112435/assignments/1943423">Project Approval</a></td>
      <td></td>
  </tr>
</table>
