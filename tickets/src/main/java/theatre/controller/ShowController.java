package theatre.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;
import theatre.entitie.Room;
import theatre.entitie.Show;
import theatre.repo.ShowRepoI;

import javax.transaction.Transactional;

@RestController
@RequestMapping("/show")
public class ShowController {

    @Autowired
    ShowRepoI repo;

    @PutMapping("/add")
    @Transactional
    public void addShow(@RequestBody Show show) {
        repo.save(show);
    }

    @GetMapping("/getByID/{id}")
    public Show getByID(@PathVariable int id) {
        return repo.getByShowID(id).orElse(null);
    }

    @GetMapping("/getByName/{name}")
    public Show getByName(@PathVariable String name) {
        return repo.getByName(name).orElse(null);
    }

    @DeleteMapping("/delete")
    @Transactional
    public void addShow(@PathVariable String name) {
        repo.deleteByName(name);
    }
}
