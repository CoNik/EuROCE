package eu.europa.euvsvirus.controller;

import org.springframework.security.access.annotation.Secured;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/healthCheck")
public class HealthCheckController {

    @RequestMapping("/ping")
    public String ping() {
        return "OK";
    }
}
