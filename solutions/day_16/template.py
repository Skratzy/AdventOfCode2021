validation = False


def debug_print(*args):
    if validation:
        print(*args)


def get_part_of_bin(bin_rep, index, length):
    bin_val = bin_rep[index:index + length]
    index += length
    return bin_val, index


def get_part_of_bin_as_int(bin_rep, index, length):
    bin_val, index = get_part_of_bin(bin_rep, index, length)
    debug_print(f'get_part_of_bin_as_int: {bin_val=}')
    return int(bin_val, 2), index


def parse_literal(bin_rep, index):
    # literal value
    literal = ""
    packets_left = True
    while packets_left:
        start, index = get_part_of_bin(bin_rep, index, 1)
        bin_val, index = get_part_of_bin(bin_rep, index, 4)
        debug_print(f'literal: {start=}, {bin_val=}')
        literal += str(bin_val)
        if start == '0':
            packets_left = False
    return literal, index


def parse_subpacket(bin_rep, index, packet_versions):
    debug_print('___Subpacket___')
    packet_version, index = get_part_of_bin_as_int(bin_rep, index, 3)
    packet_versions.append(packet_version)
    packet_id, index = get_part_of_bin_as_int(bin_rep, index, 3)
    literals = []
    if packet_id == 4:
        debug_print('___Literal___')
        debug_print(f'{bin_rep[index:]=}')
        debug_print(f'{packet_version=}, {packet_id=}')
        literal, index = parse_literal(bin_rep, index)
        debug_print(f'{literal=}, {int(literal, 2)=}, {index=}')
        return index, int(literal, 2)
    else:
        debug_print('___Operator___')
        debug_print(f'{bin_rep[index:]=}')
        debug_print(f'{packet_version=}, {packet_id=}')
        length_type_id, index = get_part_of_bin_as_int(bin_rep, index, 1)
        debug_print(f'{length_type_id=}, {index=}')
        # length type ID is 0, then the next 15 bits are a number that represents the total length in bits of the
        # sub-packets contained by this packet.
        if length_type_id == 0:
            total_length, index = get_part_of_bin_as_int(bin_rep, index, 15)
            debug_print(f'{total_length=}')
            parse_start = index
            while index - parse_start < total_length:
                keep_parsing = bin_rep[index:index + 1] == '1'
                index, literal = parse_subpacket(bin_rep, index, packet_versions)
                literals.append(literal)
            pass
        # length type ID is 1, then the next 11 bits are a number that represents the number of sub-packets immediately
        # contained by this packet.
        else:
            num_packets, index = get_part_of_bin_as_int(bin_rep, index, 11)
            debug_print(f'{num_packets=}')
            for i in range(num_packets):
                index, literal = parse_subpacket(bin_rep, index, packet_versions)
                literals.append(literal)

    ret = 0
    match packet_id:
        case 0:
            ret = sum(literals)
        case 1:
            ret = 1
            for literal in literals:
                ret *= literal
        case 2:
            ret = min(literals)
        case 3:
            ret = max(literals)
        case 5:
            ret = 1 if literals[0] > literals[1] else 0
        case 6:
            ret = 1 if literals[0] < literals[1] else 0
        case 7:
            ret = 1 if literals[0] == literals[1] else 0

    return index, ret




def part_1():
    part_1_input_file = "input.txt"
    if validation:
        part_1_input_file = "validation_part_1.txt"
    with open(part_1_input_file, "r") as file:
        # Solution here
        # First three bits = packet version
        # next three bits = packet type id
        # packets with type id 4 represent a literal value, encode a single binary number
        # other packet id is an operator that perforfm som calculation
        transmissions = file.read().split('\n')
        total_packet_versions = 0
        for line in transmissions:
            debug_print(line)
            bin_rep_size = len(line) * 4
            bin_rep = str(bin(int(line, 16)))[2:].zfill(bin_rep_size)
            debug_print(bin_rep)
            index = 0
            packet_versions = []
            parse_subpacket(bin_rep, index, packet_versions)
            #print(packet_versions)
            #print(sum(packet_versions))
            total_packet_versions += sum(packet_versions)
        return total_packet_versions


def part_2():
    part_2_input_file = "input.txt"
    if validation:
        part_2_input_file = "validation_part_2.txt"
    with open(part_2_input_file, "r") as file:
        # Solution here
        transmissions = file.read().split('\n')
        total_ret = 0
        for line in transmissions:
            bin_rep_size = len(line) * 4
            bin_rep = str(bin(int(line, 16)))[2:].zfill(bin_rep_size)
            debug_print(bin_rep)
            index = 0
            _, ret = parse_subpacket(bin_rep, index, [])
            total_ret += ret
        return ret


answer_part_1 = part_1()
answer_part_2 = part_2()
print(f'{answer_part_1=} {answer_part_2=}')
assert(answer_part_1 == 866 and answer_part_2 == 1392637195518)
