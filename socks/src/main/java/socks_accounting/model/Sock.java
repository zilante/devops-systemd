package socks_accounting.model;

import jakarta.persistence.Entity;
import jakarta.persistence.Id;
import jakarta.persistence.IdClass;
import jakarta.persistence.Table;
import jakarta.validation.constraints.Max;
import jakarta.validation.constraints.Min;
import jakarta.validation.constraints.NotBlank;
import jakarta.validation.constraints.Size;

/**
 * Entity class representing sock table from db.
 * (@color, @cottonPart) is the composite primary key.
 */
@Entity
@Table(name = "sock")
@IdClass(SockId.class)
public class Sock {
    @Id
    @NotBlank
    @Size(max = 20)
    private String color;

    @Id
    @Min(0)
    @Max(100)
    private int cottonPart;

    @Min(1)
    private int quantity;

    public Sock() {}

    public Sock(String color, int cottonPart, int quantity) {
        this.color = color;
        this.cottonPart = cottonPart;
        this.quantity = quantity;
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
