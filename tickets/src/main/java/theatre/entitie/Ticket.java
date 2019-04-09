package theatre.entitie;

import javax.persistence.*;

@Entity
@Table(name = "`Ticket`")
public class Ticket {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "ID")
    private int ticketID;

    @Column(name = "nume")
    private String name;

    @OneToOne(cascade = CascadeType.ALL, orphanRemoval = true)
    @JoinColumn(name = "UserID")
    User user;

    @OneToOne(cascade = CascadeType.ALL, orphanRemoval = true)
    @JoinColumn(name = "Show_To_Room")
    ShowToRoom showToRoom;

    public int getTicketID() {
        return ticketID;
    }

    public void setTicketID(int ticketID) {
        this.ticketID = ticketID;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public User getUser() {
        return user;
    }

    public void setUser(User user) {
        this.user = user;
    }

    public ShowToRoom getShowToRoom() {
        return showToRoom;
    }

    public void setShowToRoom(ShowToRoom showToRoom) {
        this.showToRoom = showToRoom;
    }
}