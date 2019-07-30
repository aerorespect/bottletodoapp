%#template to generate a HTML table from a list of tuples (or list of lists, or tuple of tuples or ...)
<p align="center">The open items are as follows:</p>
<table border="1" align="center">
  <tr>
    <th>id</th>
    <th>task</th>
    <th>status</th>
    <th>save</th>
  </tr>
%for row in rows:
  <tr>
    <td>{{row[0]}}</td>
    <td>{{row[1]}}</td>
    <td><select name="status">
        <option>open</option>
    %if row[2] == 0:
        <option selected>closed</option>
    %else:
        <option>closed</option>
    %end
    </td>
    <td><a href="http://localhost:8080/edit/{{row[0]}}">save</a></td>
  </tr>
%end
</table>
<a href="http://localhost:8080/new"><p style="text-align:center">create new task</p></a>
<br>
<a href="http://localhost:8080/todo"><p style="text-align:center">see open task</p></a>
<br>
<a href="http://localhost:8080/"><p style="text-align:center">see all task</p></a>