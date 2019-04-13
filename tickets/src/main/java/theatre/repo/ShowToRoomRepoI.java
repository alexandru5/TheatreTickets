package theatre.repo;

import org.springframework.data.jpa.repository.JpaRepository;
import theatre.entitie.Show;
import theatre.entitie.ShowToRoom;

import java.util.Optional;

public interface ShowToRoomRepoI extends JpaRepository<ShowToRoom, Integer> {
    @Override
    Optional<ShowToRoom> findById(Integer integer);
    Optional<ShowToRoom> getByShow(Show show);

}


