import React from 'react';
import { Button } from "@/components/ui/button";
import { Table } from "@/components/ui/table";
import { Modal } from "@/components/ui/modal";
import { FormInput } from "@/components/ui/form-input";

const SharedComponents = () => {
  return (
    <div>
      <Button className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded">
        Click me
      </Button>
      <Table className="min-w-full bg-white">
        {/* Table content */}
      </Table>
      <Modal className="fixed inset-0 flex items-center justify-center">
        {/* Modal content */}
      </Modal>
      <FormInput className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" />
    </div>
  );
};

export default SharedComponents;
