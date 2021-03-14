<html xmlns:jsp="http://java.sun.com/JSP/Page">
    <head>
        <title>Studenti</title>
    </head>
    <body>
        <h2>Informatii</h2>
        <%@ page import="beans.StudentBean" %>
        <%@ page import="java.util.ArrayList" %>
        <%  ArrayList<StudentBean> students = new ArrayList<StudentBean>();
            students = (ArrayList<StudentBean>) request.getAttribute("studenti");
        %>
        <%  for(int i = 0; i < students.size(); i++) {
        %>
            <ul type="bullet">
                <li>Nume: <%=students.get(i).getNume()%> </li>
                <li>Prenume: <%=students.get(i).getPrenume()%></li>
                <li>Varsta: <%=students.get(i).getVarsta()%></li>
            </ul>
        <br><br>
        <%}%>