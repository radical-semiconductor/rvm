module shift_reg(input  wire clk,
                 input  wire inp,
                 output wire outp);

reg flop0;
reg flop1;
reg flop2;

always @(posedge clk) begin
    flop0 <= inp;
    flop1 <= flop0;
    flop2 <= flop1;
end

assign outp = flop2;

endmodule
