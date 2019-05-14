package theatre.repo;

import org.springframework.data.domain.Example;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import theatre.entitie.Show;

import java.util.List;
import java.util.Optional;

public interface ShowRepoI extends JpaRepository<Show, Integer> {

    Optional<Show> getByShowID(Integer integer);
    Optional<Show> getByName(String name);

    void deleteByName(String name);
}
