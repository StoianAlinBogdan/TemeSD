import beans.StudentBean;
import com.fasterxml.jackson.dataformat.xml.XmlMapper;

import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.File;
import java.io.IOException;
import java.util.*;

public class ReadStudentServlet extends HttpServlet {
    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        // deserializare student din fisierul XML de pe disc
        File file = new File("/home/stoian/Documents/Java Programs/cod exemplu sd 1/JEE-Test/student.xml");

        if (!file.exists()) {
            response.sendError(404, "Nu a fost gasit niciun student serializat pe disc!");
            return;
        }

        Scanner sc = new Scanner(file);
        List<StudentBean> studenti = new ArrayList<>();
        XmlMapper xmlMapper = new XmlMapper();
        while(sc.hasNext()) {
            studenti.add(xmlMapper.readValue(sc.nextLine(), StudentBean.class));
        }
        request.setAttribute("studenti", studenti);

        // redirectionare date catre pagina de afisare a informatiilor studentului
        request.getRequestDispatcher("./view-students.jsp").forward(request, response);
    }
}
