package eu.europa.euvsvirus.controller;

import eu.europa.euvsvirus.dto.UserDto;
import eu.europa.euvsvirus.service.UserService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.access.annotation.Secured;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/user")
public class UserController {

    private UserService userService;

    @Autowired
    public UserController(UserService userService) {
        this.userService = userService;
    }

    @GetMapping("/{userId}")
    public UserDto getUser(@PathVariable int userId) {
        return userService.getUser(Long.valueOf(userId));
    }

    @PostMapping("/create")
    public String saveUser(@RequestBody UserDto userDto) {
        return userService.saveUser(userDto);
    }
}
