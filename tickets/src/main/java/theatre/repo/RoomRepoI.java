package theatre.repo;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;
import theatre.entitie.Room;

import java.util.Optional;

public interface RoomRepoI extends JpaRepository<Room, Integer> {

    Optional<Room> getByRoomID(Integer id);

    @Query("SELECT r.no_of_seats FROM Room r WHERE r.roomID=:id")
    int getNoOfSeats (@Param("id") Integer id);


}
