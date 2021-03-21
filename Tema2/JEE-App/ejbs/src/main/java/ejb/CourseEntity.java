package ejb;

import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.Id;

@Entity
public class CourseEntity {
    @Id
    @GeneratedValue
    private Integer id;
    private String nume, titular;
    private Integer credite;

    public CourseEntity()
    {

    }

    public Integer getId()
    {
        return id;
    }

    public void setId(Integer id)
    {
        this.id = id;
    }

    public String getNume() {
        return nume;
    }

    public void setNume(String nume) {
        this.nume = nume;
    }

    public String getTitular() {
        return titular;
    }

    public void setTitular(String titular)
    {
        this.titular = titular;
    }

    public Integer getCredite() {
        return credite;
    }

    public void setCredite(Integer credite)
    {
        this.credite = credite;
    }
}
