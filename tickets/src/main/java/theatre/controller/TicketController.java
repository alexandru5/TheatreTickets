package theatre.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;
import theatre.entitie.ShowToRoom;
import theatre.entitie.Ticket;
import theatre.entitie.User;
import theatre.repo.TicketRepoI;

import javax.transaction.Transactional;
import java.util.List;

@RestController
@RequestMapping("/ticket")
public class TicketController {

    @Autowired
    TicketRepoI repo;

    @PutMapping("/add")
    @Transactional
    public void addTicket(@RequestBody Ticket ticket) {
        repo.save(ticket);
    }

    @GetMapping("/getByUser")
    public List<Ticket> getAllByUser(@RequestBody User user) {
        return repo.getAllByUser(user);
    }

    @GetMapping("/getTicketToShow")
    public Ticket getByUserAndMap(@RequestBody User user, @RequestBody ShowToRoom showToRoom) {
        return repo.getByUserAndShowToRoom(user, showToRoom).orElse(null);
    }

}
