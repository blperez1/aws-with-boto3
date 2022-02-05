

class VPC:
    def __init__(self, client):
        self._client = client
        """ :type : pyboto3.ec2 """

    def create_vpc(self):
        print('Creating a VPC...')
        return self._client.create_vpc(
            CidrBlock='10.0.0.0/16'
        )

    def add_name_tag(self, resource_id, resource_name):
        print(f'Adding {resource_id} tag to the {resource_name}')
        return self._client.create_tags(
            Resources=[resource_id],
            Tags=[{
                'Key': 'Name',
                'Value': resource_name
            }]
        )

    def create_internet_gateway(self):
        print('Creating an internet gateway')
        return self.create_internet_gateway()

    def attach_igw_to_vpc(self, vpc_id, igw_id):
        print(f'Attaching Internet Gateway {igw_id} to VPC {vpc_id}')
        return self._client.attach_internet_gateway(
            InternetGatewayId=igw_id,
            VpcId=vpc_id
        )

    def create_subnet(self, vpc_id, cidr_block):
        print(f'Creating a subnet for VPC {vpc_id} with CIDR block {cidr_block}')
        return self._client.create_subnet(
            VpcId=vpc_id,
            CiderBlock=cidr_block
        )
