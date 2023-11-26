package socks_accounting.controller;

import jakarta.validation.ConstraintViolationException;
import jakarta.validation.Valid;
import jakarta.validation.constraints.Max;
import jakarta.validation.constraints.Min;
import jakarta.validation.constraints.NotBlank;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.validation.annotation.Validated;
import org.springframework.web.bind.annotation.*;
import socks_accounting.dto.SockRequest;
import socks_accounting.payload.Operation;
import socks_accounting.service.SockService;

/**
 * Controller class for handling HTTP requests
 */
@Validated
@RestController
public class Controller {
    private final SockService sockService;

    @Autowired
    public Controller(SockService sockService) {
        this.sockService = sockService;
    }

    @PostMapping("/api/socks/income")
    public ResponseEntity<String> addSocks(@Valid @RequestBody SockRequest request) {
        sockService.addSocks(request.toSock());

        return new ResponseEntity<>(
                "Socks have been added successfully!", HttpStatus.OK
        );
    }

    @PostMapping("/api/socks/outcome")
    public ResponseEntity<String> deleteSocks(
            @Valid @RequestBody SockRequest request
    ) {
        sockService.deleteSocks(request.toSock());

        return new ResponseEntity<>(
                "Socks have been deleted successfully!", HttpStatus.OK
        );
    }

    @GetMapping("/api/socks")
    public ResponseEntity<String> getSockQuantity(
            @RequestParam @NotBlank String color,
            @RequestParam Operation operation,
            @RequestParam @Min(0) @Max(100) int cottonPart
    ) {
        if (operation == Operation.NO) {
            // operation is incorrect
            return new ResponseEntity<>(HttpStatus.BAD_REQUEST);
        }

        Integer quantity = sockService.getSockQuantity(
                color, operation, cottonPart
        );

        return new ResponseEntity<>(quantity.toString(), HttpStatus.OK);
    }

    @ExceptionHandler(ConstraintViolationException.class)
    @ResponseStatus(HttpStatus.BAD_REQUEST)
    public ResponseEntity<String> handleConstraintViolationException(
            ConstraintViolationException e
    ) {
        return new ResponseEntity<>(
                "Not valid due to validation error: " + e.getMessage(),
                HttpStatus.BAD_REQUEST
        );
    }
}
