const Ethereum = {
    hex: '0x1',
    name: 'Ethereum',
    rpcUrl: '',
    ticker: "ETH"
};

const MumbaiTestnet = {
    hex: '0x13881',
    name: 'Mumbai Testnet',
    rpcUrl: '',
    ticker: "MumbaiMATIC"
};
const GoerliTestnet = {
    hex: '0x5',
    name: 'Goerli Testnet',
    rpcUrl: '',
    ticker: "GoerliEth"
};
const polygon = {
    hex: '0x137',
    name: 'polygon',
    rpcUrl: '',
    ticker: "Matic"
};
const avalanch = {
    hex: '0x43114',
    name: 'avalanch',
    rpcUrl: 'https://avalanche-mainnet.infura.io',
    ticker: "AVAX"
};


export const CHAINS_CONFIG = {
    "0x1": Ethereum,
    "0x13881": MumbaiTestnet,
    "0x5": GoerliTestnet,
    "0x137": polygon,
    "0x43114": avalanch,

};