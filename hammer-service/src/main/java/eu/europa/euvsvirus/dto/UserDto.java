package eu.europa.euvsvirus.dto;

import lombok.Getter;
import lombok.Setter;

@Getter
@Setter
public class UserDto {

    private String firstName;
    private String lastName;
    private boolean active;
    private int id;

}
