package theatre.repo;

import org.springframework.data.jpa.repository.JpaRepository;
import theatre.entitie.ShowToRoom;
import theatre.entitie.Ticket;
import theatre.entitie.User;

import java.util.List;
import java.util.Optional;

public interface TicketRepoI extends JpaRepository<Ticket, Integer> {
    @Override
    Optional<Ticket> findById(Integer integer);
    List<Ticket> getAllByUser(User user);
    Optional<Ticket> getByUserAndShowToRoom(User user, ShowToRoom showToRoom);
}
