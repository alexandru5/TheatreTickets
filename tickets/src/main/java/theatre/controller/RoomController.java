package theatre.controller;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;
import theatre.entitie.Room;
import theatre.repo.RoomRepoI;

import javax.transaction.Transactional;

@RestController
@RequestMapping("/room")
public class RoomController {

    @Autowired
    RoomRepoI repo;

    @PutMapping("/add")
    @Transactional
    public void addRoom(@RequestBody Room room) {
        repo.save(room);
    }

    @GetMapping("/getByID/{id}")
    public Room getByID(@PathVariable int id) {
        return repo.findById(id).orElse(null);
    }

    @GetMapping("/getNoOFSeats/{id}")
    public Integer getNoOFSeats(@PathVariable int id) {
        return repo.getNoOfSeats(id);
    }


}
