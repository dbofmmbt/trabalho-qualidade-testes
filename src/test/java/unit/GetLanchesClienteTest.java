package unit;

import static org.mockito.Mockito.mock;
import static org.mockito.Mockito.when;

import Controllers.getLanchesCliente;
import DAO.DaoLanche;
import Model.Lanche;
import java.io.IOException;
import java.io.PrintWriter;
import java.io.StringWriter;
import java.util.Arrays;
import javax.servlet.ServletException;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

public class GetLanchesClienteTest {

    private getLanchesCliente servlet;
    private DaoLanche daoLanche;
    private HttpServletRequest request;
    private HttpServletResponse response;
    private StringWriter stringWriter;
    private PrintWriter writer;

    @BeforeEach
    private void setupController() throws IOException {
        daoLanche = mock(DaoLanche.class);
        servlet = new getLanchesCliente(daoLanche);

        request = mock(HttpServletRequest.class);

        stringWriter = new StringWriter();
        writer = new PrintWriter(stringWriter);
        response = mock(HttpServletResponse.class);
        when(response.getWriter()).thenReturn(writer);
    }

    @Test
    public void listsAll() throws ServletException, IOException {
        Lanche hamburguer = new Lanche();
        hamburguer.setNome("hamburguer");

        Lanche pizza = new Lanche();
        pizza.setNome("pizza");

        when(daoLanche.listarTodos()).thenReturn(Arrays.asList(hamburguer, pizza));

        servlet.processRequest(request, response);

        writer.flush();
        Assertions.assertTrue(stringWriter.toString().contains(hamburguer.getNome()));
        Assertions.assertTrue(stringWriter.toString().contains(pizza.getNome()));
    }
}
