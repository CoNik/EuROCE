package eu.europa.euvsvirus.service;

import eu.europa.euvsvirus.dto.UserDto;
import eu.europa.euvsvirus.model.User;
import eu.europa.euvsvirus.repository.UserRepository;
import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.util.Optional;

@Slf4j
@Service
@Transactional
public class UserService {

    private UserRepository userRepository;

    @Autowired
    public UserService(UserRepository userRepository) {
        this.userRepository = userRepository;
    }

    public String saveUser(UserDto userDto){

        User user = new User();
        user.setFirstName(userDto.getFirstName());
        user.setLastName(userDto.getLastName());
        user.setActive(true);
        return userRepository.save(user).getFirstName();
    }

    public UserDto getUser(Long userId){
        User user = userRepository.findById(userId).orElseThrow(() ->new RuntimeException());
        return transform(user);
    }

    private UserDto transform(User user) {
    UserDto userDto = new UserDto();
    userDto.setFirstName(user.getFirstName());
    userDto.setLastName(user.getLastName());
    userDto.setActive(user.isActive());
    userDto.setId(user.getId().intValue());
    return userDto;
    }
}
