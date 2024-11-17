

const data = [
    {
        id: '728ed52f',
        amount: 100,
        status: 'pending',
        email: 'm@example.com'
    },
    {
        id: '489e1d42',
        amount: 125,
        status: 'processing',
        email: 'example@gmail.com'
    },
    {
        id: 'a1b2c3d4',
        amount: 150,
        status: 'success',
        email: 'user1@example.com'
    },
    {
        id: 'e5f6g7h8',
        amount: 200,
        status: 'failed',
        email: 'user2@example.com'
    },
    {
        id: 'i9j0k1l2',
        amount: 175,
        status: 'pending',
        email: 'user3@example.com'
    },
    {
        id: 'm3n4o5p6',
        amount: 225,
        status: 'processing',
        email: 'user4@example.com'
    }
];

export async function load() {
    return {
        data,
    };
}
