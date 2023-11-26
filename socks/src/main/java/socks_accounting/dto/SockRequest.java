package socks_accounting.dto;

import jakarta.validation.constraints.Max;
import jakarta.validation.constraints.Min;
import jakarta.validation.constraints.NotBlank;
import jakarta.validation.constraints.Size;
import socks_accounting.model.Sock;

public class SockRequest {

    @NotBlank
    @Size(max = 20)
    private String color;

    @Min(0)
    @Max(100)
    private int cottonPart;

    @Min(1)
    private int quantity;

    public Sock toSock() {
        return new Sock(
            color,
            cottonPart,
            quantity
        );
    }

    public String getColor() {
        return color;
    }

    public int getCottonPart() {
        return cottonPart;
    }

    public int getQuantity() {
        return quantity;
    }

    public void setQuantity(int quantity) {
        this.quantity = quantity;
    }
}
