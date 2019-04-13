package theatre.repo;

import org.springframework.data.jpa.repository.JpaRepository;
import theatre.entitie.Show;

import java.util.Optional;

public interface ShowRepoI extends JpaRepository<Show, Integer> {

    Optional<Show> getByShowID(Integer integer);
    Optional<Show> getByName(String name);

}
