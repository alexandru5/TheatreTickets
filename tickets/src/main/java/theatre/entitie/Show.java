package theatre.entitie;

import javax.persistence.*;

@Entity
@Table(name = "`Show`")
public class Show {

    @Id
    @GeneratedValue(strategy= GenerationType.IDENTITY)
    @Column(name = "UserID")
    private int showID;

    @Column(name = "Name")
    private String name;

    @Column(name = "No_of_Tickets")
    private int no_of_tickets;

    @Column(name = "Price_per_Ticket")
    private int price_per_ticket;

    @Column(name = "Date")
    private String date;

    @Column(name = "Hour")
    private String hour;


    public int getShowID() {
        return showID;
    }

    public void setShowID(int showID) {
        this.showID = showID;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public int getNo_of_tickets() {
        return no_of_tickets;
    }

    public void setNo_of_tickets(int no_of_tickets) {
        this.no_of_tickets = no_of_tickets;
    }

    public int getPrice_per_ticket() {
        return price_per_ticket;
    }

    public void setPrice_per_ticket(int price_per_ticket) {
        this.price_per_ticket = price_per_ticket;
    }

    public String getDate() {
        return date;
    }

    public void setDate(String date) {
        this.date = date;
    }

    public String getHour() {
        return hour;
    }

    public void setHour(String hour) {
        this.hour = hour;
    }
}