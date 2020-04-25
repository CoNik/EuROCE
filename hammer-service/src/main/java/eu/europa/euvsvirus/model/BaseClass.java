package eu.europa.euvsvirus.model;

import lombok.Getter;
import lombok.Setter;
import org.hibernate.annotations.GenericGenerator;

import javax.persistence.*;
import java.util.UUID;

@Getter
@Setter
@MappedSuperclass
public class BaseClass {

    @Id
    @GeneratedValue(
            generator = "sequence",
            strategy = GenerationType.SEQUENCE
    )
    @SequenceGenerator(
            name = "sequence",
            allocationSize = 10
    )
    @Column(name = "id", unique = true, nullable = false)
    private Long id;

}