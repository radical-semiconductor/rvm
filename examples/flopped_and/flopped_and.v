module flopped_and(input  wire clk,
                   input  wire A,
                   input  wire B,
                   output reg  C);

    always @(posedge clk) begin
        C <= A & B;
    end

endmodule
