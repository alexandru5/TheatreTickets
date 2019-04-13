package theatre.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;
import theatre.entitie.Show;
import theatre.entitie.ShowToRoom;
import theatre.repo.ShowRepoI;
import theatre.repo.ShowToRoomRepoI;

import javax.transaction.Transactional;

@RestController
@RequestMapping("/map")
public class ShowToRoomController {

    @Autowired
    ShowToRoomRepoI repo;

    @PutMapping("/add")
    @Transactional
    public void addShowToRoom(@RequestBody ShowToRoom showToRoom) {
        repo.save(showToRoom);
    }

    @GetMapping("/getByShow")
    public ShowToRoom getByShow(@RequestBody Show show) {
        return repo.getByShow(show).orElse(null);
    }

}


